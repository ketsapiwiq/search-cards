<template>
  <div class="container-fluid">
    <div class="form-group">
    <p>Cards search:</p>
     <!-- {{ cards }} -->
        <form class="searchForm" v-on:submit.prevent="submitSearch">
      <input class="form-control" type="text" v-model="searchQuery" placeholder="Type here" @keyup="getCards">
        </form>
    </div>
    <div class="card-columns">
      <div class="card" v-for="card in cards" v-bind:key="card">
        <div class="card-body">
          <h5 class="card-title">{{ card.title }}</h5>
          <p class="card-text">{{ card.text }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// Vue.filter('htmlEscape', function(value) {
//   return value.replace(/\&amp\;/g, '&');
// });

export default {
  data () {
    return {
      cards: null,
      searchQuery: ''
    }
  },
  methods: {
    getCards () {
      const path = `http://localhost:5000/api/cards/`
      var request = path + this.searchQuery
      axios.get(request)
      .then(response => {
        this.cards = response.data.cards
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    this.getCards()
  }
}
</script>
