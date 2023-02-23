import { createStore } from 'vuex'

export default createStore({
  state: {
    stock: {},
  },
  getters: {
  },
  mutations: {
    curStock(state, stock){
      state.stock=stock
      console.log(state.stock)
    }
  },
  actions: {
  },
  modules: {
  }
})
