import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import MenuView from '../views/MenuView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import CurrentView from '../views/CurrentView.vue'
import StockbuyView from '../views/StockbuyView.vue'
import SearchView from '../views/SearchView.vue'
import CartView from '../views/CartView.vue'
import CreateView from '../views/CreateView.vue'
import CartbuyView from '../views/CartbuyView.vue'
import testView from '../views/testView.vue'

const routes = [
  {
    path: '/index',
    name: 'index',
    component: IndexView
  },
  {
    path: '/menu',
    name: 'menu',
    component: MenuView
  },
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/current',
    name: 'current',
    component: CurrentView
  },
  {
    path: '/stockbuy',
    name: 'stockbuy',
    component: StockbuyView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/cartbuy',
    name: 'cartbuy',
    component: CartbuyView
  },
  {
    path: '/test',
    name: 'test',
    component: testView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
