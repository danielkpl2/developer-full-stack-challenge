<template>
    <div>
        <b-container >
            <b-row>
                <b-col sm="2" v-if="parent_author_id === undefined">
                    Page {{ currentPage }} of {{ totalPages }}, showing {{ fromItems }} - {{ toItems }} of {{ total }}
                    items.
                </b-col>
                <b-col sm="1" v-if="parent_author_id === undefined">
                    <b-button id="prev-page" @click="prevPage" :disabled="!canGoBack">&#8592;Back</b-button>
                </b-col>
                <b-col sm="1" v-if="parent_author_id === undefined">
                    <b-button id="next-page" @click="nextPage" :disabled="!canGoNext">Next&#8594;</b-button>
                </b-col>
                <b-col sm="3" v-if="parent_author_id === undefined">
                    <b-form-input v-model="search" placeholder="Search Book"></b-form-input>
                </b-col>
                <b-col sm="3">
                    <b-button id="show-btn" @click="addBook">Add Book</b-button>
                </b-col>
            </b-row>
        </b-container>
        <b-table striped hover :items="items" :fields="fields" @row-clicked="onRowClicked"></b-table>

        <b-modal ref="add-book" hide-footer title="Add New Book">
            <b-row>
                <b-col sm="3">
                    <label :for="book_name">Name:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input :id="book_name" v-model="book_name" placeholder="Book Name"></b-form-input>
                </b-col>
            </b-row>
            <b-row>
                <b-col sm="3">
                    <label :for="number_pages">Number of pages:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input id="number_pages" v-model="number_pages" placeholder="Number of pages"
                        type="number"></b-form-input>
                </b-col>
            </b-row>
            <b-row>
                <b-col sm="3">
                    <label :for="author_id">Author ID:</label>
                </b-col>
                <b-col sm="9">
                    <treeselect
                        v-model="author_id" 
                        :value="author_id" 
                        :multiple="false" 
                        :async="true" 
                        :options="options" 
                        :load-options="loadOptions" />
                </b-col>
            </b-row>
            <b-row>
                <b-button id="save-book" @click="saveBook">Add Book</b-button>
            </b-row>
        </b-modal>

        <b-modal ref="edit-book" hide-footer title="Edit Book">
            <b-row>
                <b-col sm="3">
                    <label :for="book_name">Name:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input id="book_name" v-model="book_name" placeholder="Book Name"></b-form-input>
                </b-col>
            </b-row>

            <b-row>
                <b-col sm="3">
                    <label :for="number_pages">Number of pages:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input id="number_pages" v-model="number_pages" placeholder="Number of pages"
                        type="number"></b-form-input>
                </b-col>
            </b-row>
            <b-row>
                <b-col sm="3">
                    <label :for="author_id">Author ID:</label>
                </b-col>
                <b-col sm="9">
                    <treeselect
                        v-model="author_id" 
                        :value="author_id" 
                        :multiple="false" 
                        :async="true" 
                        :options="options" 
                        :load-options="loadOptions" />
                </b-col>
            </b-row>

            <b-row>
                <b-button id="save-book" @click="patchBook">Save Book</b-button>
            </b-row>
        </b-modal>
    </div>
</template>

<script>
import Treeselect, { ASYNC_SEARCH } from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
export default {
    middleware: 'authenticated',
    components: { Treeselect },
    props: ['parent_author_id'],
    data() {
        return {
            items: [],
            fields: ["name", "number_pages", "author.name"],
            search: "",
            limit: 10,
            offset: 0,
            total: 0,
            author_id: null,
            author_name: "",
            book_id: 0,
            book_name: "",
            number_pages: 0,
            options: [],
        }
    },
    mounted() {
        if (this.parent_author_id !== undefined) {
            this.author_id = this.parent_author_id
        }
    },
    methods: {
        async loadOptions({ action, searchQuery, callback }) {
            if (action === ASYNC_SEARCH) {
                let { items } = await this.$axios.$get(`/authors?limit=20&offset=0&search=${searchQuery}`)
                let options = items.map(item => ({
                    id: item.id,
                    label: item.name
                }))
                callback(null, options)
            }
        },
        nextPage() {
            if (this.canGoNext) {
                this.offset = this.offset + this.limit
                this.$fetch()
            }
        },
        prevPage() {
            if (this.canGoBack) {
                this.offset = this.offset - this.limit
                this.$fetch()
            }
        },
        showModal(modalId) {
            this.$refs[modalId].show()
        },
        hideModal(modalId) {
            this.$refs[modalId].hide()
        },
        addBook() {
            this.book_name = ""
            this.showModal('add-book')
        },
        async onRowClicked(item) {
            this.book_id = item.id
            this.book_name = item.name
            this.number_pages = item.number_pages
            this.$nextTick()
            this.options = [{id: item.author.id, label: item.author.name}]
            this.author_id = item.author.id
            this.showModal('edit-book')
        },
        normalizer(author) {
            return { id: author.id, label: author.name };
        },
        async saveBook() {
            this.hideModal('add-book')
            console.log('book_name', this.book_name)
            try {
                let response = await this.$axios.$post("/books", {
                    name: this.book_name,
                    number_pages: this.number_pages,
                    author_id: this.author_id
                })
                this.$fetch()
            } catch (error) {
                console.log(error)
            }
        },
        async patchBook() {
            this.hideModal('edit-book')
            try {
                let response = await this.$axios.$patch(`/books/${this.book_id}`, {
                    id: this.book_id,
                    name: this.book_name,
                    number_pages: this.number_pages,
                    author_id: this.author_id
                })
                this.$fetch()
            } catch (error) {
                console.log(error)
            }
        },
    },
    computed: {
        currentPage() {
            return Math.floor(this.offset / this.limit) + 1
        },
        totalPages() {
            return Math.ceil(this.total / this.limit)
        },
        fromItems() {
            return this.offset + 1
        },
        toItems() {
            return Math.min(this.offset + this.limit, this.total)
        },
        canGoBack() {
            return this.offset - this.limit >= 0
        },
        canGoNext() {
            return this.offset + this.limit < this.total
        }
    },
    async fetch() {
        let parent_author_id = ""
        if (this.parent_author_id !== undefined) {
            parent_author_id = `author_id=${this.parent_author_id}`
        }
        let { items, limit, offset, total } = await this.$axios.$get(`/books?limit=${this.limit}&offset=${this.offset}&search=${this.search}&${parent_author_id}`)
        this.items = items
        this.limit = limit
        this.offset = offset
        this.total = total
    },
    watch: {
        search(newSearch, oldSearch) {
            this.$fetch()
        },
    }
}
</script>