<script setup>
import { ref, onMounted, computed } from 'vue'
// import axios from 'axios';
import { useAuthStore } from '@/stores/auth.js'

const authStore = useAuthStore()
const csrfToken = computed(() => {
  const cookie = document.cookie
    .split('; ')
    .find((row) => row.startsWith('csrftoken='))
  return cookie ? decodeURIComponent(cookie.split('=')[1]) : ''
})

// const currentUser = ref(null)
// const isLoaading = ref(true)

// Вычисляем отображаемое имя
// const displayName = computed(() => {
//     if (!currentUser.value) {
//         return '';
//     } else {
//         return currentUser.value.full_name || currentUser.value.username;
//     }
// });

// Запрос текущего пользователя
// const whoAmI = async () => {
//     try {
//         const response = await axios.get('/api/users/me/')
//         if (response.data.is_authenticated) {
//             currentUser.value = response.data.user
//         } else {
//             currentUser.value = null
//         }
//     } catch (error) {
//         console.error('Ошибка при получении пользователя:', error)
//         currentUser.value = null
//     } finally {
//         isLoading.value = false
//     }
// }

// Выход из системы
// const logout = async () => {
//     try {
//         await axios.post('/accounts/logout/')
//         // После выхода обновляем состояние
//         currentUser.value = null
//         // Можно перенаправить на главную
//         window.location.href = '/'
//     } catch (error) {
//         console.error('Ошибка при выходе:', error)
//     }
// }

onMounted(() => {
  if (!authStore.isLoaded) {
    authStore.loadCurrentUser()
  }
})
</script>

<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Online Store</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Каталог</a>
          </li>
          <li v-if="authStore.isManager" class="nav-item">
            <a class="nav-link" href="products/create">Создать товар</a>
          </li>
        </ul>

        <div class="d-flex align-items-center gap-2">
          <!-- Если пользователь авторизован -->
          <template v-if="authStore.isAuthenticated">
            <span class="text-body-secondary small">
              {{ authStore.displayName }}
            </span>

            <form v-if="authStore.isAuthenticated" method="post" action="/accounts/logout/" class="mb-0">
              <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken" />
              <button type="submit" class="btn btn-outline-secondary btn-sm">
                Выйти
              </button>
            </form>
          </template>

          <!-- Если не авторизован -->
          <template v-else>
            <a href="/accounts/login/" class="btn btn-primary btn-sm">Войти</a>
            <!-- Или можно сделать свою страницу регистрации -->
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>
