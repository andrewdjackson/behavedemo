// main.go
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

// Article - Our struct for all articles
type Article struct {
	Id      string `json:"Id"`
	Title   string `json:"Title"`
	Desc    string `json:"desc"`
	Content string `json:"content"`
}

var Articles []Article

func homePage(w http.ResponseWriter, r *http.Request) {
	html := `
	<form action="login" method="post">
	<div class="container">
		<label for="username"><b>Username</b></label>
		<input type="text" placeholder="Enter Username" name="username" required>

		<label for="password"><b>Password</b></label>
		<input type="password" placeholder="Enter Password" name="password" required>

		<button type="submit">Login</button>
	</div>
	</form>
	`
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, html)
	fmt.Println("Endpoint Hit: homePage")
}

func homePageLogin(w http.ResponseWriter, r *http.Request) {
	success := "<p name='login' id='login'>success</p>"
	failure := "<p name='login' id='login'>failed</p>"
	username := r.FormValue("username")
	password := r.FormValue("password")
	valid := false

	fmt.Println("Endpoint Hit: login ", username, password)

	if username == "user1" && password == "pass1" {
		valid = true
	}

	if username == "user2" && password == "pass2" {
		valid = true
	}

	w.Header().Set("Content-Type", "text/html; charset=utf-8")

	if valid {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintf(w, success)
	} else {
		w.WriteHeader(http.StatusUnauthorized)
		fmt.Fprintf(w, failure)
	}
}

func returnAllArticles(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: returnAllArticles")
	json.NewEncoder(w).Encode(Articles)
}

func returnSingleArticle(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	key := vars["id"]
	fnd := false

	fmt.Println("Endpoint Hit: returnSingleArticle ", key)

	for _, article := range Articles {
		if article.Id == key {
			json.NewEncoder(w).Encode(article)
			fnd = true
		}
	}

	if !fnd {
		w.WriteHeader(http.StatusNotFound)
	}
}

func findArticleById(id string) Article {
	for _, article := range Articles {
		if article.Id == id {
			return article
		}
	}

	return Article{}
}

func createNewArticle(w http.ResponseWriter, r *http.Request) {
	// get the body of our POST request
	// unmarshal this into a new Article struct
	// append this to our Articles array.
	reqBody, _ := ioutil.ReadAll(r.Body)

	var article Article
	_ = json.Unmarshal(reqBody, &article)

	fmt.Println("Endpoint Hit: createNewArticle ", article)

	existingArticle := findArticleById(article.Id)

	if existingArticle.Id == article.Id {
		fmt.Println("Endpoint Hit: article exists")
		article = existingArticle
	} else {
		// update our global Articles array to include
		// our new Article
		Articles = append(Articles, article)
	}

	_ = json.NewEncoder(w).Encode(article)
}

func deleteArticle(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]

	fmt.Println("Endpoint Hit: deleteArticle ", id)

	for index, article := range Articles {
		if article.Id == id {
			Articles = append(Articles[:index], Articles[index+1:]...)
		}
	}

}

func handleRequests() {
	myRouter := mux.NewRouter().StrictSlash(true)
	myRouter.HandleFunc("/", homePage)
	myRouter.HandleFunc("/login", homePageLogin).Methods("POST")
	myRouter.HandleFunc("/articles", returnAllArticles)
	myRouter.HandleFunc("/article", createNewArticle).Methods("POST")
	myRouter.HandleFunc("/article/{id}", deleteArticle).Methods("DELETE")
	myRouter.HandleFunc("/article/{id}", returnSingleArticle)
	log.Fatal(http.ListenAndServe(":10000", myRouter))
}

func main() {
	Articles = []Article{
		Article{Id: "1", Title: "Hello", Desc: "Article Description", Content: "Article Content"},
		Article{Id: "2", Title: "Hello 2", Desc: "Article Description", Content: "Article Content"},
	}

	fmt.Println("Server running on http://localhost:10000")

	handleRequests()
}
