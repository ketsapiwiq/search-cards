<template>
  <div class="card">
    <div class="edit-card" 
        v-if="(edit || isAdding)">
      <form>
        <span v-if="isAdding"
        <input type="hidden" name="card_id" 
        :value="this.id" v-if="this.id" != undefined
         />
        <table class="card-inputs">
          <tr v-model="card.data"
            v-bind:key="index" v-for="(value, key, index) in card.data" >
        <td><input v-on:keyup.enter="setCard" @blur="setCard" type="text" :value="key" /></td>
        <td><input type="text" :value="value" /></td>
        <td><button @click="deleteRow(index)">Delete</button></td>
        </tr>
        <button class="btn-info" @click="addRow">Add</button>
        <button class="btn-info" @click="setCard">Validate</button>

        </table>
      </form>
    </div>
      <table v-else @click="edit = true;" class="display-card table-sm table-striped">
        <tr v-for="(value, key) in card.data">
          <td>
            <i>{{ key }}</i>
          </td>
          <td>{{ value }}</td>
        </tr>
        <!-- <tr><pre class="card-data">{{ card.data }}</pre></tr> -->
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    data: {
      type: Object,
      default: function () { return {'': ''} }

    },
    isAdding: Boolean
  },
  data () {
    return {
      // isAdding: false,
      // card: {'data': {'title': ''}},
      edit: false,
      index: 0
    }
  },

  methods: {
    setCard () {
      const path = `http://localhost:5000/api/cards/`
      var request = path
      if (!this.isAdding) {
        request = path + this.id
      }
      axios
        .post(request, this.data)
        .then(response => {
          if (this.isAdding) { this.isAdding = !(response.status === 200) }
        })
        .catch((error) => {
          console.log(error)
        })
    },
    addRow () {
      this.data.push({'': ''})
    },
    deleteRow (index) {
      this.data.splice(index, 1)
    }
  },
  updated () {
    this.setCard()
  }
  // computed: {
  //   keyname: function (key) {
  //     return 'key-' + key
  //   },
  //   valuename: function (key, value) {
  //     return 'value-' + value
  //   }
  // },
  // mounted () {
  //   // var doc = jsyaml.load('greeting: hello\nname: world');
  //   this.jsonString =
  //     typeof this.card !== 'undefined' ? JSON.stringify(this.card.data) : '{}'
  //   // this.jsonString = JSON.stringify(this.card.data)
  // },
  // watch: {
  // jsonString: function (newValue) {
  //   try {
  //     let newCardData = JSON.parse(newValue)
  //     this.card.data = newCardData
  //   } catch (err) {
  //     console.log('seems to be invalid json: ' + err)
  //     // reset:
  //     this.jsonString = JSON.stringify(this.card.data)
  //   }
  // }
  // }
  // directives: {
  //  focus: {
  //    inserted (el) {
  //      el.focus()
  //    }
  //  }
  // }
}
</script>