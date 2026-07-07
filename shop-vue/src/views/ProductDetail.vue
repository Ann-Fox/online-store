<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { Product } from '@/api';

const route = useRoute()
const product = ref(null)
const isLoading = ref(true);

const getProduct = async () => {
  isLoading.value = true;
  try {
    const id = route.params.id;
    if (!id) {
      product.value = null;
      return;
    }
    const data = await Product.getById(id);
    product.value = data;
  } catch (error) {
    console.error('Ошибка загрузки товара:', error);
    product.value = null;
  } finally {
    isLoading.value = false;
  }
};


onMounted(getProduct)
</script>

<template>
 <div v-if="isLoading" class="container py-4 text-center">
    Загрузка...
  </div>

<div v-else-if="product" class="container py-4">
    <!-- Хлебные крошки -->
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="/">Главная</a></li>
            <li class="breadcrumb-item"><a href="/">Каталог</a></li>
            <li v-if="product.category_name " class="breadcrumb-item">
                <a href="">{{ product.category_name  }}                    </a>
            </li>
            <li class="breadcrumb-item active" aria-current="page">
        {{ product.name }}
    </li>
        </ol>
    </nav>

    <div class="row g-5">
        <!-- Левая колонка: изображение -->
        <div class="col-md-6">
            <div class="position-relative">
                <img v-if="product.image" :src="product.image" class="img-fluid rounded shadow" alt="" />
                <div v-else class="bg-light text-center p-5 rounded shadow" style="
                height: 400px;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                    <span class="text-muted">Нет изображения</span>
                </div>
                <!-- Бейдж с категорией (поверх изображения) -->
                <span v-if="product.category_name" class="badge bg-success position-absolute top-0 start-0 m-3">
                    {{ product.category_name }}
                </span>
            </div>
        </div>

        <!-- Правая колонка: информация о товаре -->
        <div class="col-md-6">
            <h1 class="display-5 fw-bold">{{ product.name }}</h1>
            <p class="text-muted mb-3">{{ product.description }}</p>

            <!-- Цена и кнопка -->
            <div class="d-flex align-items-center gap-3 mb-4">
                <span class="display-6 fw-bold text-success"> {{ product.price }}₽</span>
                <a href="#" class="btn btn-success btn-lg px-5">Добавить в корзину</a>
            </div>

            <!-- Дополнительные характеристики (если есть) -->
            <p v-if="product.quantity !== undefined" class="text-muted">
                <i class="bi bi-box"></i> Доступно: {{ product.quantity }} шт.
            </p>
        </div>
    </div>

</div>

</template>