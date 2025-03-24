import requests

# Define the base API URL
API_URL = "https://jsonplaceholder.typicode.com/posts"

# Function to perform a GET request
def get_post(post_id):
    try:
        response = requests.get(f"{API_URL}/{post_id}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ GET Request Successful: Fetched Post {post_id}\n")
            print(f"Title: {data['title']}\nBody:\n{data['body']}\n")
        else:
            print(f"❌ GET Error: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ GET Request Failed: {e}")

# Function to perform a POST request (Create new post)
def create_post():
    new_post = {
        "title": "New Post",
        "body": "This is a new post created via API.",
        "userId": 1
    }
    try:
        response = requests.post(API_URL, json=new_post)
        if response.status_code == 201:
            data = response.json()
            print(f"✅ POST Request Successful: Created New Post\n")
            print(f"Post ID: {data['id']}\nTitle: {data['title']}\nBody:\n{data['body']}\n")
            return data['id']  # Return the new post ID for further operations
        else:
            print(f"❌ POST Error: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ POST Request Failed: {e}")

# Function to perform a PUT request (Update existing post)
def update_post(post_id):
    updated_post = {
        "id": post_id,
        "title": "Updated Post",
        "body": "This post has been updated via API.",
        "userId": 1
    }
    try:
        response = requests.put(f"{API_URL}/{post_id}", json=updated_post)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ PUT Request Successful: Updated Post {post_id}\n")
            print(f"Title: {data['title']}\nBody:\n{data['body']}\n")
        else:
            print(f"❌ PUT Error: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ PUT Request Failed: {e}")

# Function to perform a DELETE request
def delete_post(post_id):
    try:
        response = requests.delete(f"{API_URL}/{post_id}")
        if response.status_code == 200 or response.status_code == 204:
            print(f"✅ DELETE Request Successful: Post {post_id} Deleted\n")
        else:
            print(f"❌ DELETE Error: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ DELETE Request Failed: {e}")

# Main execution
if __name__ == "__main__":
    # Step 1: Fetch a post
    get_post(1)

    # Step 2: Create a new post
    new_post_id = create_post()

    if new_post_id:
        # Step 3: Update the created post
        update_post(new_post_id)

        # Step 4: Delete the created post
        delete_post(new_post_id)