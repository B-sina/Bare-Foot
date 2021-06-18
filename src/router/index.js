import { createRouter, createWebHistory } from 'vue-router'
import home from '../components/home.vue'
import about from '../components/about.vue'
import contact from '../components/contact.vue'
import login from '../components/login.vue'
import shops from '../components/shops.vue'
import signup from '../components/signup.vue'
import cart from '../components/cart.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path: '/about',
    name: 'About',
    component:about
  },
  {
    path: '/contact',
    name:'Contact',
    component:contact
  },

  {
    path: '/shops/:id',
    name:'shops',
    props: true,
    component:shops
  },
  {
    path: '/login',
    name:'login',
    component:login
  },
  {
    path: '/signup',
    name:'signup',
    component:signup
  },
  {
    path: '/cart',
    name:'cart',
    component:cart
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
