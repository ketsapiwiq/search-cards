<template>
  <div class="container-fluid">
    <div class="form-group">
    <p>Cards search:</p>
     <!-- {{ cards }} -->
        <form class="searchForm" v-on:submit.prevent="submitSearch">
      <input class="form-control" type="text" v-model="searchQuery" placeholder="Type here" @keyup="getCards">
        </form>
    </div>
    <div class="add-card">
      <a class="btn btn-primary" href="#" v-on:click="isAdding = !isAdding">Add a card</a>
    </div>

    <Card isAdding v-if="isAdding" />

    <div class="card-columns">
      <div v-for="card in cards" v-bind:key="card.id">
        <Card v-bind:card='card' />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import Card from './Card.vue'

export default {
  components: {
    Card
  },
  data () {
    return {
      cards: null,
      searchQuery: '',
      isAdding: false
    }
  },
  methods: {
    getCards () {
      const path = `http://localhost:5000/api/cards/search/`
      var request = path + this.searchQuery
      axios.get(request)
        .then(response => {
          // this.cards = response.data.cards
          this.cards = response.data
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
