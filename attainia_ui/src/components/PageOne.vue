<template>
  <div class="about">
    <h1>Table 1 component</h1>
  </div>
</template>

<script>
// import axios from 'axios'; 
export default {
  created(){
    // axios.get('http://localhost:8000/users/', {headers: {"Access-Control-Allow-Origin":"http://localhost:8000", "Access-Control-Allow-Credentials": "true"}})
    // .then(res =>{
    //   console.log(res.data);
    // })
    // .catch(err => console.log(err));

    fetch("http://localhost:8000/users/").then(function (response) {
      console.log(response);
            // return response.json();
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>