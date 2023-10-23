import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'

import HelloWorld from './components/HelloWorld.vue'
import Dogs from './pages/Dogs.vue'

const routes = [
    {path:'/hello', component: HelloWorld, name:'helloworld'},
    {path:'/dogs', component: Dogs, name:"dogs"},
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

const app = createApp(App)

app.use(router)

app.mount('#app')

