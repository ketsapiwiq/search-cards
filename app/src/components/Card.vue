<template>
  <!-- <div class="card" :class="this.card.id" > -->
  <div class="card" :class="card.id">
    <!-- id: {{ card.id }} -->
    <textarea
      v-if="edit"
      @blur.native="jsonString = $event.target.data; edit = false; $emit('input', jsonString);"
      @keyup.enter.native="jsonString = $event.target.data; edit = false; $emit('input', jsonString);"
      v-focus
      v-model="jsonString"
    ></textarea>
    <table v-else @click="edit = true;" class="display-card table-sm  table-striped">
      <tr :class="key" v-for="(value, key) in card.data" v-bind:key="key">
        <td>
          <i>{{ key }}</i>
        </td>
        <td>{{ value }}</td>
      </tr>
      <!-- <tr><pre class="card-data">{{ card.data }}</pre></tr> -->
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['card'],
  data () {
    return {
      edit: false,
      jsonString: this.card.data
    }
  },

  methods: {
    setCard () {
      const path = `http://localhost:5000/api/cards/`
      var request = path + this.card.id
      axios
        .post(request, this.card.data)
        // .then(response => {
        //   // this.cards = response.data.cards
        //   this.cards = response.data
        // })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  updated () {
    this.setCard()
  },

  mounted () {
    this.jsonString = JSON.stringify(this.card.data)
  },
  watch: {
    jsonString: function (newValue) {
      try {
        let newCardData = JSON.parse(newValue)
        this.card.data = newCardData
      } catch (err) {
        console.log('seems to be invalid json: ' + err)
        // reset:
        this.jsonString = JSON.stringify(this.card.data)
      }
    }
  },
  directives: {
    focus: {
      inserted (el) {
        el.focus()
      }
    }
  }
}
</script>