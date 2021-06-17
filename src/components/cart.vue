<template>

<div id="cart" class="container">
  <header>
      quantity:{{cart.length}}
      <button class="btn btn-primary" v-on:click="navigateTo('cart')">view Cart</button>
  </header>
  <div v-if="pages === 'cart'">
    <h1>products</h1>
    <div class="products">
      <div v-for="products in product" :key="products.name">
        {{products.name}}
        <img :src="products.item_picture" />
        <div>{{products.price}}</div>
        <div>{{products.description}}</div>
        <button v-on:click="getcarts(product)">Add To Cart</button>
      </div>
    </div>
  </div>
  <div v-if="pages === 'product'">
    <h1>products</h1>
    <div class="products">
      <div v-for="products in product" :key="products.name">
        {{products.name}}
        <img :src="products.item_picture" />
        <div>{{products.price}}</div>
        <div>{{products.description}}</div>
        <button v-on:click="getcarts(product)">Add To Cart</button>
      </div>
    </div>
  </div>
  <h1 class="mt-5 mb-4" style="font-weight:300">Cart</h1>
<div class="cart-table">

   <div class="row cart-row">
   <div class="col-xs-12 col-md-2">
  </div>
  <div class="col-md-6" >
    <div class="product ">
          <p>Products Name: {{product.name}}</p>
          <p>Prices:{{product.price}}</p>
       <div class="product-delete">
      <button type="button" data-toggle="tooltip" title="Ta bort" class="delete" onclick="cart.remove('5');"><strong>X</strong></button><br>
      <button type="button" v-on:click='getcarts(product)' ><strong>ADD</strong></button>
      </div>
   </div>

</div>
</div>
</div><!-- cart-row-->
 
  
</div>
    
</template>
<script>
export default {
    name:"cart",
    
    data() {
        return {
          pages:"cart",
          cart:[],
            product:{}
        }
    },
    props:{
        id:{
            type:[Number, String], 
            required:true
        }
    },
    methods: {
      getcarts(product){
        this.cart.push(product)
        console.log(this.cart);
      },
      navigateTo(pages){
        this.pages = pages;
      }
      ,
        getproductsData(){
            fetch(`http://127.0.0.1:5100/products/${this.id}`, {
                method: 'GET',
                headers: {
                    "Content-Type" : "application/json"
                }
            })
            .then(resp => resp.json())
            .then(data => {
                this.product = data
                // console.log(data);
            })
            .catch(error => { 
                console.log(error);
            })
        }
    },
    created(){
        this.getproductsData()
    }
    
    
}
</script>
<style>
.cart-row{padding:15px 0}
.cart-row:nth-child(even){background:#efefef}
.product-name{font-size:16px;font-weight:600}
.product-options{font-size:12px;margin-bottom:5px}
.product-options span{color:#666;font-weight:400;text-transform:uppercase}
.product-articlenr{color:#666;font-weight:400;text-transform:uppercase}
.product-price small{color:#666;font-weight:300;font-size:20px;margin:0;padding:0;line-height:initial}
.cart-table .cart-row input{width:30px;height:auto;padding:2px;border-radius:0;border-color:#000;float:left;font-size:14px;text-align:center}
.cart-table .cart-row button.update{border:0;padding:7px 8px;background:#000;color:#fff;font-size:9px;float:left;margin-right:5px}
.cart-table .cart-row button.delete{background-color:#FFB2B2;color:#000!important;padding:7px 13px;font-size:13px;border:0;border-radius:50px}
.product-price-total{font-size:16px;font-weight:400;width:80%;float:left}
.cart-actions{display:flex;justify-content:center;align-items:center}
.cart-special-holder{background:#efefef}
.cart-special{padding:1em 1em 0;display:block;margin-top:.5em;border-top:1px solid #dadada}
.cart-special .cart-special-content:before{content:"\21b3";font-size:1.5em;margin-right:1em;color:#6f6f6f;font-family:helvetica,arial,sans-serif}
</style>