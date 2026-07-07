import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App.vue'
import router from './router'
import '@/assets/main.css'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const app = createApp(App)
app.use(createPinia())
app.use(router)

// app.mount('#app')

// Функция загрузки настроек
async function loadSettings() {
    try {
        const response = await axios.get('/api/settings/')
        const color = response.data.primary_color || '#0d6efd'
        document.documentElement.style.setProperty('--btn-primary-bg', color)
        document.documentElement.style.setProperty('--btn-primary-border', color)
    } catch (error) {
        console.error('Ошибка загрузки настроек:', error)
    }
}

loadSettings().then(() => {
    const app = createApp(App)
    app.use(createPinia())  // ← обязательно подключаем Pinia
    app.use(router)
    app.mount('#app')
})