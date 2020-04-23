<script>
import { onMount } from 'svelte';
import Cookies from 'js-cookie/src/js.cookie.js';

let books = [];

const CSRF_TOKEN = Cookies.get('csrftoken');
const INDEX_URL = getRef("library-ref");

function getRef(id) {return document.getElementById(id).href;};

onMount(async () => {
	const response = await fetch(INDEX_URL, {
								  headers: {
									'Accept': 'application/json, text-plain, */*',
									'X-Requested-With': 'XMLHttpRequest',
								  }
	});
	let books_from_json = await response.json();
	books = books_from_json['books'];
	books = books;

	console.log(books);    
    });


</script>

<main>
	
	<div class="section-intro pb-60px">
          <p>Awesome books</p>
          <h2>Trending <span class="section-intro__style"> books</span></h2>
        </div>
        <div class="row">
			{#each books as book}
			<div class="col-md-6 col-lg-4 col-xl-3">
            <div class="card text-center card-product">
              <div class="card-product__img">
                <img class="card-img" src="#" alt="">
                <ul class="card-product__imgOverlay">
                  <li><button><i class="ti-search"></i></button></li>
                  <li><button><i class="ti-shopping-cart"></i></button></li>
                  <li><button><i class="ti-heart"></i></button></li>
                </ul>
              </div>
              <div class="card-body">
                <p>{book.genre}</p>
                <h4 class="card-product__title"><a href="#">{book.title}</a></h4>
                <p class="card-product__price">{book.author}</p>
              </div>
            </div>
          </div>
		  {/each}
		  
        </div>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>