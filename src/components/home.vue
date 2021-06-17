<template>
  <div id="home">
    <!-- Modal -->
    <div
      class="modal fade bg-white"
      id="templatemo_search"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-lg" role="document">
        <div class="w-100 pt-1 mb-5 text-right">
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form
          action=""
          method="get"
          class="modal-content modal-body border-0 p-0"
        >
          <div class="input-group mb-2">
            <input
              type="text"
              class="form-control"
              id="inputModalSearch"
              name="q"
              placeholder="Search ..."
            />
            <button
              type="submit"
              class="input-group-text bg-success text-light"
            >
              <i class="fa fa-fw fa-search text-white"></i>
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Start Banner Hero -->
    <div
      id="template-mo- Bado Eger-hero-carousel"
      class="carousel slide"
      data-bs-ride="carousel"
    >
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="container">
            <div class="row p-5">
              <div class="mx-auto col-md-8 col-lg-6 order-lg-last">
                <img class="img-fluid" src="" alt="" />
              </div>
              <div class="col-lg-6 mb-0 d-flex align-items-center">
                <div class="text-align-left align-self-center">
                  <h1 class="h1 text-success"><b> Bado Eger</b> eCommerce</h1>
                  <h3 class="h2">Tiny and Perfect Shoe Shopping</h3>
                  <p>
                    Bado Eger Shop is an eCommerce Website concerned with the
                    selling of premium shoes with great quality.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <a
        class="carousel-control-prev text-decoration-none w-auto ps-3"
        href="#template-mo- Bado Eger-hero-carousel"
        role="button"
        data-bs-slide="prev"
      >
        <i class="fas fa-chevron-left"></i>
      </a>
      <a
        class="carousel-control-next text-decoration-none w-auto pe-3"
        href="#template-mo- Bado Eger-hero-carousel"
        role="button"
        data-bs-slide="next"
      >
        <i class="fas fa-chevron-right"></i>
      </a>
    </div>
    <!-- End Banner Hero -->

    <!-- Start Featured Product -->
    <section class="bg-light row">
      <div class="container mt-5  ">
                <div class="container">
            <div class="row">


          <div class="col-md-4 " v-for="product in products" :key="product.id">
            <div class="card mb-4 product-wap rounded-0 d-flex">
              <div class="card rounded-0">
                <img
                  class="card-img rounded-0 img-fluid"
                  v-bind:src="product.item_picture"
                />
                <div
                  class="
                    card-img-overlay
                    rounded-0
                    product-overlay
                    d-flex
                    align-items-center
                    justify-content-center
                  "
                ></div>
              </div>
              <div class="card-body">
                <h3 >
                  <router-link
                    class="link-style h3name"
                    :to="{ name: 'shops', params: { id: product.id } }"
                  >
                    {{ product.name }}
                  </router-link>
                </h3>
                <ul
                  class="
                    w-100
                    list-unstyled
                    d-flex
                    justify-content-between
                    mb-0
                  "
                >
                  <li>M/L/X/XL</li>
                  <li class="pt-2">
                    <span
                      class="product-color-dot
                        color-dot-red
                        float-left
                        rounded-circle
                        ml-1
                      "
                    ></span>
                    <span
                      class="
                        product-color-dot
                        color-dot-blue
                        float-left
                        rounded-circle
                        ml-1
                      "
                    ></span>
                    <span
                      class="
                        product-color-dot
                        color-dot-black
                        float-left
                        rounded-circle
                        ml-1
                      "
                    ></span>
                    <span
                      class="
                        product-color-dot
                        color-dot-light
                        float-left
                        rounded-circle
                        ml-1
                      "
                    ></span>
                    <span
                      class="
                        product-color-dot
                        color-dot-green
                        float-left
                        rounded-circle
                        ml-1
                      "
                    ></span>
                  </li>
                </ul>
                <ul class="list-unstyled d-flex justify-content-center mb-1">
                  <li>
                    <i class="text-warning fa fa-star"></i>
                    <i class="text-warning fa fa-star"></i>
                    <i class="text-warning fa fa-star"></i>
                    <i class="text-muted fa fa-star"></i>
                    <i class="text-muted fa fa-star"></i>
                  </li>
                </ul>
                <p class="text-center mb-0">${{ product.price }}</p>
                <p class="text-center mb-0">{{ product.description }}</p>
              </div>
            </div>
          </div>
                </div>        
        </div>
      </div>
    </section>
    <!-- End Featured Product -->
  </div>
</template>
<script>
export default {
  name: "home",
  // components:{

  // },
  data() {
    return {
      products: [],
    };
  },
  methods: {
    getproducts() {
      fetch("http://127.0.0.1:5100/product", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.products.push(...data);
          // console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getproducts();
  },
};
</script>
<style scoped>
.h3name{
  text-decoration: none;
  color: green;
}
</style>