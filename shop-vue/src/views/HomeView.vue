<script setup>
import { onMounted, ref } from 'vue'
// import axios from 'axios'
import { Product, ProductImage, ProductCategory } from '@/api'


const productList = ref([])
// const product_image = ref([])
const search = ref('')

const productCategory = ref('')
const productCategories = ref([])
// Загрузка категорий
const getProductCategory = async () => {
  productCategories.value = await ProductCategory.getList()
}

// Загрузка товаров с фильтрами
const getProductList = async () => {
  const filters = {
    search: search.value,
    category: productCategory.value
  }

  // Удаляем пустые параметры
  if (!filters.search) delete filters.search
  if (!filters.category) delete filters.category // передаём выбранную категорию

  // let res = await axios.get('/api/product/?search=' + search.value)
  const res = await Product.getList(filters)
  console.log(res)
  productList.value = res.results || res // если без пагинации, то просто массив

  // let res_product_image = await ProductImage.getList()
  // console.log(res_product_image);
  // product_image.value = res_product_image.results
}


const resetFilter = () => {
  productCategory.value = ''
  getProductList()
}

onMounted(() => {
  getProductList()
  getProductCategory()
})
</script>

<template>
  <div class="container">
    <!-- {{ product_image }} -->
    <!-- Поле поиска -->
    <input v-model="search" @input="getProductList" placeholder="Поиск..." class="form-control mb-3" />

    <!-- Фильтр по категориям -->
    <div class="row mb-4">
      <div class="col-md-12">
        <div class="row g-3 align-items-center"></div>
        <!-- <form method="get" @submit.prevent="getProductList" class="row g-3"> -->
        <div class="col-auto mt-3">
          <label for="categoryFilter" class="visually-hidden">Категория</label>
          <select v-model="productCategory" name="category" id="categoryFilter" class="form-select"
            @onchange="getProductList">
            <option value="">Все категории</option>
            <option v-for="category in productCategories" :value="category.value" :key="category.value">
              {{ category.label }}
            </option>
          </select>
        </div>
        <div class="col-auto mt-2 d-flex gap-3">
          <button @click.prevent="getProductList" class="btn btn-outline-success">
            Применить
          </button>
          <button @click.prevent="resetFilter" class="btn btn-secondary">Сбросить</button>
        </div>
        <!-- </form> -->
      </div>
    </div>



     <div class="row gy-5">
    <template v-if="productList.length > 0">
      <div class="col-4" v-for="product in productList">
        <div class="card" style="width: 18rem">
          <img v-if="product.image" :src="product.image" class="card-img-top" :alt="product.name"
            style="height: 200px; object-fit: cover" />
          <div v-else class="card-img-top bg-light d-flex align-items-center justify-content-center"
            style="height: 200px; color: #6c757d">
            Нет фото
          </div>
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <h5 class="card-title">{{ product.name }}</h5>
              <div class="d-flex flex-column">
                <span class="badge bg-success">{{ product.category_name }}</span>
              </div>

            </div>

            <p class="card-text">{{ product.description }}</p>
            <p class="card-text"><strong>{{ product.price }} ₽</strong></p>
            <!-- <a href="" class="btn btn-success">К товару</a> -->
            <RouterLink class="btn btn-success" :to="{name: 'product-detail', params: {id: product.id}}">К товару</RouterLink>
          </div>
        </div>
      </div>
    </template>
  </div>
  </div>

 

</template>
