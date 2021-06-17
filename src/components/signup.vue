<template>
  <div id="signup">
    <section>
      <hgroup>
        <h2>Welcome back!</h2>
        <p>Please enter your details to sign into your account</p>
      </hgroup>

      <form  class="log-form" @submit.prevent="createUser">
        <div class="group log-input">
          <input
            type="text"
            id="fullname"
            name="fullname"
            placeholder="Full Name" v-model= "full_name"
          />
        </div>
        <div class="group log-input">
        <input
            type="password"
            id="pass"
            name="passwords"
            placeholder="Password"
            v-model= "password"
          />
          </div>
        <div class="group log-input">
        <input
            type="text"
            id="email"
            name="email"
            placeholder="E-mail"
          v-model= "email"
          />
          </div>

        <!-- <div class="group  upload-form-btn">
          <input
            type="file"
            name="avatar"
            @change="onFileSelected"
          />
          <button class="upload-form-btn" @click="onUpload">Upload</button>
        </div> -->

        <span class="check left-align">
          <label>Already have an account?</label>
          <router-link to="/login"
            :class="activePage == 'login' ? 'active' : ''"
            >Log In</router-link>
        </span>

        <br /><br />

        <div class="container-log-btn">
           <button type="submit" name="btn_submit" class="log-form-btn" ><span>Sign Up</span> 
          </button>
        </div>
      </form>
      <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5" role="alert">
        <strong>{{error}}</strong>
      </div>
    </section>
  </div>
</template>
<script>

export default {
  name: "signup",
  components: {},
  data(){
    return{
      full_name:'',
      password:'',
      selectedFile:null,
      e_mail:'',
      
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
      createUser(){
        if(!this.full_name|| !this.email|| !this.password){
          this.error = "Please Fill all fields"
        }
        else{
          fetch("http://127.0.0.1:5100/register", {
                 method: 'POST',
                headers: {
                    "Content-Type" : "application/json"
                },
                body:JSON.stringify({'full_name':this.full_name, 'password':this.password, 'email':this.email})
            })
            .then(resp => resp.json())
            .then((b) => {
              console.log(b);
                this.$router.push({
                  name:"home"
                })
            })
            .catch(error => { 
                console.log(error);
            })

        }
            
        }
  }

};

</script>
<style scoped>
* {
  box-sizing: border-box;
}

body {
  background: #eee;
}

hgroup {
  text-align: center;
  margin-top: 4em;
}

span {
  font-size: 0.95em;
  font-weight: 600;
  line-height: 24px;
}

/*------------------------------------------------------------------
[ Login Form ]*/

.log-form {
  width: 500px;
  margin: 4em auto;
  padding: 3em 2em 2em 2em;
  background: #fafafa;
  border: 1px solid #ebebeb;
  box-shadow: rgba(0, 0, 0, 0.14902) 0px 1px 1px 0px,
    rgba(0, 0, 0, 0.09804) 0px 1px 2px 0px;
}

.group {
  position: relative;
  margin-bottom: 45px;
}

.log-input {
  font-size: 18px;
  padding: 10px 10px 10px 5px;
  -webkit-appearance: none;
  display: block;
  background: #fafafa;
  color: #636363;
  width: 100%;
  border: none;
  border-radius: 0;
  border-bottom: 1px solid #757575;
}

.log-input:focus {
  outline: none;
}

.log-form a {
  font-size: 8px;
  color: coral;
}

.left-align {
  float: left;
  text-align: left;
}

.right-align {
  float: right;
  text-align: right;
}

/*------------------------------------------------------------------
[ Button same code as contact form ]*/

.container-log-btn {
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding-top: 50px;
}

.log-form-btn {
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 20px;
  min-width: 250px;
  height: 50px;
  background-color: transparent;
  border-radius: 7px;
  cursor: pointer;

  font-size: 16px;
  color: whitesmoke;
  line-height: 1.2;
  text-transform: uppercase;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
  position: relative;
  z-index: 1;
}
.upload-form-btn {
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 10px;
  min-width: 50px;
  height: 40px;
  background-color: coral;
  border-radius: 7px;
  cursor: pointer;

  font-size: 16px;
  color: whitesmoke;
  line-height: 1.2;
  text-transform: uppercase;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
  position: relative;
  z-index: 1;
}
.log-form-btn::before {
  content: "";
  display: block;
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  top: 0;
  left: 50%;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  border-radius: 7px;
  background-color: coral;
  pointer-events: none;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
}

.log-form-btn:hover:before {
  background-color: #916439;
}

input[type="text"],
input[type="email"],
input[type="password"],
textarea,
select {
  background: transparent;
  border: none;
  font-family: "Montserrat";
  font-size: 12px;
  font-weight: 400;
  letter-spacing: 0.2em;
  line-height: 24px;
  height: 42px;
  padding-left: 20px;
  padding-right: 20px;
  text-transform: none;
  width: 100%;
}

input[type="checkbox"]:not(:checked) + label,
input[type="checkbox"]:checked + label {
  color: #aaaaaa;
  cursor: pointer;
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 0.3em;
  padding-left: 10px;
  padding-top: 6px;
  position: relative;
  text-transform: uppercase;
}
/* added */
label {
  font-size: 9px;
  font-family: "Courier New", Courier, monospace;
}
.loginn {
  text-decoration: none;
  font-size: 8px;
  color: coral;
}
</style>