window.addEventListener("load", async () => {
  const response = await fetch("/get_articles").then((res) => res.json());
  console.log(response);
  let articleList = response.articles.map((item) => {
    return `
    <div onclick="detail(${item.id})">
        <input type="hidden" value="${item.id}"/>
        ${item.title} <br />
        <br />
        ${item.content}
        <br />
        <i>작성자: ${item.author}</i>
        <a href="articles/edit/${item.id}">글 수정</a>
        <a href="articles/destroy/${item.id}">글 삭제</a>
    </div>`;
  });
  document.querySelector(".article-list").innerHTML = articleList;
});

const detail = (articleId) => {
  location.href = `/articles/${articleId}`;
};
