<template>
<div id="contact">
    
    <!-- Modal -->
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


    <!-- Start Content Page -->
    <div class="container-fluid bg-light py-5">
        <div class="col-md-6 m-auto text-center">
            <h1 class="h1">Contact Us</h1>
            <p>
                We are a prominent two trying to do our best in the community we live in. If you
                have any questions just ask us through our socials.
            </p>
        </div>
    </div>

    <!-- Start Contact -->
    <div class="container py-5">
        <div class="row py-5">
            <form class="col-md-9 m-auto" action="https://formspree.io/f/xjvjrprq" method="POST" role="form">
                <div class="row">
                    <div class="form-group col-md-6 mb-3">
                        <label for="inputname">Name</label>
                        <input type="text" class="form-control mt-1" id="message" name="name" placeholder="Name">
                    </div>
                    <div class="form-group col-md-6 mb-3">
                        <label for="inputemail">Email</label>
                        <input type="email" class="form-control mt-1" id="message" name="email" placeholder="Email">
                    </div>
                </div>
                <div class="mb-3">
                    <label for="inputsubject">Subject</label>
                    <input type="text" class="form-control mt-1" id="message" name="subject" placeholder="Subject">
                </div>
                <div class="mb-3">
                    <label for="inputmessage">Message</label>
                    <textarea class="form-control mt-1" id="message" name="message" placeholder="Message" rows="8"></textarea>
                </div>
                <div class="row">
                    <div class="col text-end mt-2">
                        <button type="submit" class="btn btn-success btn-lg px-3">Let’s Talk</button>
                    </div>
                </div>
                
            </form>
        </div>
    </div>
    <!-- End Contact -->


</div>
    
</template>
<script>
export default {
    name:"shop",
    components:{

    }
    
}
</script>
<style scoped>
.message{
    background-color: aliceblue;
}
#status.success{
    padding: 10px;
    background-color: aquamarine;
    border-radius: 8px;
    animation: status 4s ease forwards;
}
#status.error{
    padding: 10px;
    background-color: red;
    color: black;
    border-radius: 8px;
    animation: status 4s ease forwards;
}
@keyframes status{
    0%{
        opacity: 1;
        pointer-events:all;

    }
    90%{
        opacity: 1;
        pointer-events:all;

    }
    100%{
        opacity: 1;
        pointer-events:none;

    }
}
</style>