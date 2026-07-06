import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App.vue'
import router from './router'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const app = createApp(App)
app.use(createPinia())
app.use(router)

app.mount('#app')


// import axios from 'axios'

// // Функция для получения CSRF-токена из cookie
// function getCSRFToken() {
//   const cookieValue = document.cookie
//     .split('; ')
//     .find(row => row.startsWith('csrftoken='))
//   return cookieValue ? cookieValue.split('=')[1] : null
// }

// // Устанавливаем базовый URL для всех запросов (опционально)
// axios.defaults.baseURL = process.env.VUE_APP_API_URL || '/'

// // Добавляем интерсептор для отправки CSRF-токена
// axios.interceptors.request.use(config => {
//   const token = getCSRFToken()
//   if (token) {
//     config.headers['X-CSRFToken'] = token
//   }
//   return config
// })