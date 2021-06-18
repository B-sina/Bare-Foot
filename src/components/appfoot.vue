<template>

  <div id ="appfoot">
    <footer class="bg-transparent" id="tempaltemo_footer">
        <div class="container">
            <div class="row">

                <div class="col-md-4 pt-5">
                    <h2 class="h2 text-success border-bottom pb-3 border-light logo"> Bado Eger Shop</h2>
                    <ul class="list-unstyled text-dark footer-link-list">
                        <li>
                            <i class="fas fa-map-marker-alt fa-fw"></i>
                            123 Consectetur at ligula 10660
                        </li>
                        <li>
                            <i class="fa fa-phone fa-fw"></i>
                            <a class="text-decoration-none" href="tel:010-020-0340">+251945905405 , +251925596549</a>
                        </li>
                        <li>
                            <i class="fa fa-envelope fa-fw"></i>
                            <a class="text-decoration-none" href="mailto:info@company.com">danmekonnnen@gmail.com , it.sintayehu.sermessa@gmail.com</a>
                        </li>
                    </ul>
                </div>

                <div class="col-md-4 pt-5">
                    <div class="col-auto me-auto">
                        <h2 class="h2 text-dark border-bottom pb-3 border-light">Links</h2>
                        <ul class="list-inline text-left footer-icons">
                            <li class="list-inline-item border border-light rounded-circle text-center">
                                <a class="text-dark text-decoration-none" target="_blank" href="https://www.facebook.com/dan.mekonnen.94"><i class="fab fa-facebook"></i></a>
                            </li>
                            <li class="list-inline-item border border-light rounded-circle text-center">
                                <a class="text-dark text-decoration-none" target="_blank" href="https://www.instagram.com/sintayehu_sermessa/"><i class="fab fa-instagram"></i></a>
                            </li>
                            <li class="list-inline-item border border-light rounded-circle text-center">
                                <a class="text-dark text-decoration-none" target="_blank" href="https://twitter.com/Dan_Mekonnen"><i class="fab fa-twitter"></i></a>
                            </li>
                            <li class="list-inline-item border border-light rounded-circle text-center">
                                <a class="text-dark text-decoration-none" target="_blank" href="https://www.linkedin.com/in/sintayehu-sermessa-185783209/"><i class="fab fa-linkedin"></i></a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="col-md-4 pt-5">
                    <h2 class="h2 text-dark border-bottom pb-3 border-light">Further Info</h2>
                    <ul class="list-unstyled text-dark footer-link-list text-decoration">
                        <li><router-link to="/" :class="activePage == 'home' ? 'active' : ''"
                >Home</router-link
              ></li>
                        <li><router-link
                to="/about"
                :class="activePage == 'about' ? 'active' : ''"
                >About</router-link
              ></li>
                        
                        <li><router-link
                to="/contact"
                :class="activePage == 'contact' ? 'active' : ''"
                >Contact</router-link></li>
                    </ul>
                </div>

            </div>

           
        </div>

        <div class="w-100 bg-black py-3">
            <div class="container">
                <div class="row pt-2">
                    <div class="col-12">
                        <p class="text-left text-dark">
                            Copyright &copy; 2021 Bado Feet
                        </p>
                    </div>
                </div>
            </div>
        </div>

    </footer>
  </div>

</template>

<script>


export default {
  name: 'appfoot',
  components: {
    
  }
}
</script>

<style scoped>
#app {


}
</style>
