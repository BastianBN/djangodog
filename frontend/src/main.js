import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'

import Accueil from './components/Accueil.vue'
import Dogs from './pages/Dogs.vue'

const routes = [
    {path:'/', component: Accueil, name:'accueil'},
    {path:'/dogs', component: Dogs, name:"dogs"},
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

const app = createApp(App)

app.use(router)

app.mount('#app')

