class RequestManager {
  static async getPosts() {
    const payload = await fetch("/api/get_posts");
    const posts = await payload.json();
    return posts;
  }
}

export {RequestManager};
