<template>
<div id="admin">
        <div class="container py-5">
        <div class="row py-5">
            <form class="col-md-9 m-auto" @submit.prevent="adminster" action="https://formspree.io/f/xjvjrprq" method="POST" role="form">
                <div class="row">
                    <div class="form-group col-md-8 mb-3">
                        <label for="inputname">Shoe Name</label>
                        <input v-model= "name" type="text" class="form-control mt-1" id="message" name="name" placeholder="Name">
                    </div>
                    <div class="form-group col-md-4 mb-3">
                        <label for="inputemail">Price</label>
                        <input  v-model= "price" type="number" class="form-control mt-1" id="message" name="price" placeholder="price">
                    </div>
                </div>
                <div class="row">
                    <div class="form-group col-md-8 mb-3">
                        <label for="inputname">Catagory</label>
                        <input  v-model= "catagory" type="text" class="form-control mt-1" id="message" name="name" placeholder="Catagory">
                    </div>
                    <div class="form-group col-md-4 mb-3">
                        <label for="inputemail">Shoe Size</label>
                        <input v-model= "shoe_size" type="number" class="form-control mt-1" id="message" name="price" placeholder="Shoe Size">
                    </div>
                </div>
                <div class="mb-3">
                    <label for="inputmessage">Description</label>
                    <textarea v-model= "description" class="form-control mt-1" id="message" name="message" placeholder="Description" rows="8"></textarea>
                </div>
                <div>
                    <label for="inputmessage">Image Url</label>
                    <input v-model= "item_picture" type="text" class="form-control mt-1" id="message" name="price" placeholder="https://google.com/dashfkjhd87adfa">

                </div>

                <!--  -->
                <div>
                    <label for="inputmessage">Avaliable</label>
                    <input v-model= "avaliable" type="number" class="form-control mt-1" id="message" name="price" placeholder="1 or 0">

                </div>
                <!--  -->
                
                


                
                <div class="row">
                    <div class="col text-end mt-2">
                        <button type="submit" class="btn btn-success btn-lg px-3">Add Item</button>
                    </div>
                </div>
                
            </form>
        </div>
    </div>
</div>
    
</template>
<script>

export default {
  name: "admin",
  components: {},
  data(){
    return{
      name:'',
      price:'',
      catagory:'',
      shoe_size:'',
      description:'',
      item_picture:'',
      avaliablity:'',
      
    }
  },
  methods:{
    
      handleSubmit(){
       const data = {
         full_name : this.full_name,
         password:this.password,
         email: this.email,
         error:null

       }
        console.log(data)
      },
      
      onFileSelected(){
        this.selectedFile = event.target.files[0]

      },
      onUpload(){

      },
      adminster(){
        if(this.name|| this.price|| this.catagory||this.shoe_size||this.description||this.item_picture||this.avaliablity){
          fetch("http://127.0.0.1:5100/product", {
                 method: 'POST',
                headers: {
                    "Content-Type" : "application/json"
                },
                body:JSON.stringify({'name':this.name, 'price':this.price, 'categories':this.catagory,'shoe_size':this.shoe_size,'description':this.description,'item_picture':this.item_picture, 'avaliablility':this.avaliablity})
            })
            .then(resp => resp.json())
            .then((b) => {
              console.log(b);
                this.$router.push({
                  name:"admin"
                })
            })
            .catch(error => { 
                console.log(error);
            })
          
          
         
        }
        else{
           this.error = "Please Fill all fields"
          console.log('empty');

        }
            
        }
  }

};

    

</script>
<style scoped>
/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>