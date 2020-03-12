<template>
  <div class="home">
    <HelloWorld msg="Table 1"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Page1',
  components: {
    HelloWorld
  }
}
</script>
