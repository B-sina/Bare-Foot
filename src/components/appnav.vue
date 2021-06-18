<template>
  <nav class="navbar navbar-expand-lg navbar-light shadow">
    <div class="container d-flex justify-content-between align-items-center">
      <router-link class="navbar-brand text-success logo h1 align-self-center" to="/" :class="activePage == 'home' ? 'active' : ''"
                >Bado Eger</router-link
              >

      <button
        class="navbar-toggler border-0"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#templatemo_main_nav"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div
        class="
          align-self-center
          collapse
          navbar-collapse
          flex-fill
          d-lg-flex
          justify-content-lg-between
        "
        id="templatemo_main_nav"
      >
        <div class="flex-fill">
          <ul class="nav navbar-nav d-flex justify-content-center mx-lg-auto">
            <li class="nav-item mx-3">
              <router-link to="/" :class="activePage == 'home' ? 'active' : ''"
                >Home</router-link
              >
            </li>
            <li class="nav-item mx-3">
              <router-link
                to="/about"
                :class="activePage == 'about' ? 'active' : ''"
                >About</router-link
              >
            </li>
            <li class="nav-item mx-3">
              <router-link
                to="/contact"
                :class="activePage == 'contact' ? 'active' : ''"
                >Contact</router-link>
            </li>
          </ul>
        </div>
        <div class="navbar align-self-center d-flex">
          <div class="d-lg-none flex-sm-fill mt-3 mb-4 col-7 col-sm-auto pr-3">
            <div class="input-group">
              <input
                type="text"
                class="form-control"
                id="inputMobileSearch"
                placeholder="Search ..."
              />
              <div class="input-group-text">
                <i class="fa fa-fw fa-search"></i>
              </div>
            </div>
          </div>
          <a
            class="nav-icon d-none d-lg-inline"
            href="#"
            data-bs-toggle="modal"
            data-bs-target="#templatemo_search"
          >
            <i class="fa fa-fw fa-search text-dark mr-2"></i>
          </a>
          <a class="nav-icon position-relative text-decoration-none" href="#">
            <router-link
              to="/cart"
              :class="activePage == 'cart' ? 'active' : ''"
              ><i class="fa fa-fw fa-cart-arrow-down text-dark mr-1"></i
            ></router-link>
          </a>
          <a class="nav-icon position-relative text-decoration-none" href="#">
            <router-link
              to="/login"
              :class="activePage == 'login' ? 'active' : ''"
              ><i class="fa fa-fw fa-user text-dark mr-3"></i
            ></router-link>
          </a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "appnav",
  components: {},
};
</script>

<style scoped>
#app {
}
#templatemo_nav_top {
  min-height: 40px;
}
#templatemo_nav_top * {
  font-size: 0.9em !important;
}
#templatemo_main_nav a {
  color: #212934;
  text-decoration: none;
}
#templatemo_main_nav a:hover {
  color: #e86100;
}
#templatemo_main_nav .navbar .nav-icon {
  margin-right: 20px;
}
</style>