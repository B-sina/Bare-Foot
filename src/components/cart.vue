<template>
  <!-- <cartitemCart 
  v-for="item in items" :key="item.id"
  :item = "item"/> -->
  <div class = "mt-5" v-for="item in items" :key="item.id">
    <p>{{item.name}}</p>
    <p>${{item.price}}</p>

  </div>
  <!-- <h3>total :{{item.quantity}} * {{item.price}}</h3>
  <h4>Total cost: {{total_quantity}}</h4> -->
</template>

<script>
// import cartitemCart from '../components/cart/cartitemCart.vue'
export default {
  // components :{
  //   cartitemCart
  // },
  
   mounted(){
    this.$store.commit('updateCartFromLocalStoreage')

  },
  computed: {
    items() {
      return this.$store.getters.cartItems
    },
    total_quantity(){
      return this.$store.item.quantity
    }
    // item_cost(){
    //         return this.itemxx.price * this.itemxx.quantity
    //     }
  }
}
</script>

<style>

</style>