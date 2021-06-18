<template>
  <div class="cart-item-card">
        <div class="header">
            <h3>{{item.name}}</h3>\
            <h4>In cart: {{item.quantity}}</h4>
            <h4>Total cost: {{item_cost.toFixed(2)}}</h4>
        </div>
        <p> {{description}} </p>
    </div>
</template>

<script>
import { computed } from '@vue/runtime-core'
export default {
    props:['item'],
    computed: {
        // description(){
        //     return this.item.description.substring(0,120)
        // },
        item_cost(){
            return this.item.price * this.item.quantity
        }
    }
}
</script>

<style>

</style>
