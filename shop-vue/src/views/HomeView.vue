<script setup>
import {onMounted, ref} from 'vue'
// import axios from 'axios'
import { Product, ProductImage } from '@/api'


const productList = ref([])
const product_image = ref([])
const search = ref('')

const getProductList = async()=>{
  // let res = await axios.get('/api/product/?search=' + search.value)
  let res = await Product.getList({search: search.value})
  console.log(res)
  productList.value = res.results
  let res_product_image = await ProductImage.getList()
  console.log(res_product_image);
  product_image.value = res_product_image.results
}

onMounted(()=>{
  getProductList()
})
</script>

<template>
  <div class="container">
   {{ product_image }}
    <input v-model="search" @input="getProductList">
    <!-- Фильтр по категориям -->
    <div class="row mb-4">
      <div class="col-md-12">
        <form method="get" class="row g-3">
          <div class="col-auto">
            <label for="categoryFilter" class="visually-hidden">Категория</label>
            <select name="category" id="categoryFilter" class="form-select" onchange="this.form.submit()">
              <option value="">Все категории</option>
              <option value="">
              </option>
            </select>
          </div>
          <div class="col-auto">
            <button type="submit" class="btn btn-outline-success">
              Применить
            </button>
            <a href="" class="btn btn-secondary">Сбросить</a>
          </div>
        </form>
      </div>
    </div>
    <div class="row gy-5">
      <div class="col-4" v-for="product in productList">
        <div class="card" style="width: 18rem">
           <img
           v-if="product.image"
          :src="product.image"
          class="card-img-top"
          :alt="product.name"
          style="height: 200px; object-fit: cover"
        />
          <div v-else class="card-img-top bg-light d-flex align-items-center justify-content-center"
            style="height: 200px; color: #6c757d">
            Нет фото
          </div>
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text">{{ product.description }}</p>
            <p class="card-text"><strong>{{ product.price }} ₽</strong></p>
            <a href="" class="btn btn-success">К товару</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
