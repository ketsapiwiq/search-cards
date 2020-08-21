<script>
export default {
  data: {
    finds: []
  },
  methods: {
    addFind: function () {
      this.finds.push({ value: 'def' })
    },
    deleteFind: function (index) {
      console.log(index)
      console.log(this.finds)
      this.finds.splice(index, 1)
    }
  }
}
</script>


<template>
  <div id="app">
    <h1>Finds</h1>
    <div v-for="(find, index) in finds">
      <input v-model="find.value" />
      <button @click="deleteFind(index)">delete</button>
    </div>

    <button @click="addFind">New Find</button>

    <pre>{{ $data }}</pre>
  </div>
</template>
