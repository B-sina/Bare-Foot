<template>
<div id="shops">
    <div class="container mt-5">
        <div class="modal fade bg-white" id="templatemo_search" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="w-100 pt-1 mb-5 text-right">
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <form action="" method="get" class="modal-content modal-body border-0 p-0">
                <div class="input-group mb-2">
                    <input type="text" class="form-control" id="inputModalSearch" name="q" placeholder="Search ...">
                    <button type="submit" class="input-group-text bg-success text-light">
                        <i class="fa fa-fw fa-search text-white"></i>
                    </button>
                </div>
            </form>
        </div>
    </div>



    <!-- Open Content -->
    <section class="bg-light">
        <div class="container pb-5">
            <div class="row">
                <div class="col-lg-5 mt-5">
                    <div class="card mb-3">
                        <img
                  class="card-img rounded-0 img-fluid"
                  v-bind:src="product.item_picture"
                />
                    </div>
                    <div class="row">
                    </div>
                </div>
                <!-- col end -->
                <div class="col-lg-7 mt-5">
                    <div class="card">
                        <div class="card-body">
                            <h1 class="h2">{{product.name}}</h1>
                            <p class="h3 py-2">${{product.price}}</p>
                            <ul class="list-inline">
                                <li class="list-inline-item">
                                    <h6>Brand:</h6>
                                </li>
                                <li class="list-inline-item">
                                    <p class="text-muted"><strong>Easy Wear</strong></p>
                                </li>{}
                            </ul>

                            <h6>Description:</h6>
                            <p>{{product.description}}</p>
                            <ul class="list-inline">
                                <li class="list-inline-item">
                                    <h6>Avaliable Color :</h6>
                                </li>
                                <li class="list-inline-item">
                                    <p class="text-muted"><strong>White / Black</strong></p>
                                </li>
                            </ul>
                            <div v-if="product_total" class="product_total">
                                <h3> In Cart</h3>
                                <h4> {{product_total}}</h4>
                            </div>

                            <div class="button-container">
                                <button class="remove btn btn-danger" @click="removeFromCart()">Remove</button> 

                                <button  class="add btn btn-info" @click="addToCart()">Add To Cart</button>
                            </div>
                            <!-- <form action="" method="GET">
                                <input type="hidden" name="product-title" value="Activewear">
                                
                                <div class="row pb-3">
                                    
                                    <div class="col d-grid">
                                        <router-link
                    class="link-style"
                    :to="{ name: 'cart', params: { id: product.id } }"
                  >
                    <button type="submit" class="btn btn-success btn-lg" name="submit" value="addtocard">add to cart</button>
                  </router-link>
                                        
                                    </div>
                                </div>
                            </form> -->

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Close Content -->

    <!-- Start Article -->

       
  </div>
</div>
    
</template>
<script>
export default {

    name:"shops",
      props:{
        id:{
            type:[Number, String], 
            required:true
        }

    },
    computed:{
        product_total(){
            return this.$store.getters.productQuantity(this.product)
    },

    },
    data() {
        return {
            product:{}
        }
    },
  
    
    methods: {
        addToCart(){
            this.$store.commit('addToCart' , this.product)
        },
        removeFromCart(){
            this.$store.commit('removeFromCart', this.product)
        },
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
<style scoped>

</style>