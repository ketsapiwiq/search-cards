<template>
  <div class="hello"><textarea v-model="jsonString"></textarea></div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      foo: {
        some: 'some',
        other: 'other'
      },
      jsonString: ''
    }
  },
  mounted () {
    this.jsonString = JSON.stringify(this.foo)
  },
  watch: {
    jsonString: function (newValue) {
      try {
        let newFoo = JSON.parse(newValue)
        this.foo = newFoo
      } catch (err) {
        console.log('seems to be invalid json: ' + err)
        // reset:
        this.jsonString = JSON.stringify(this.foo)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
