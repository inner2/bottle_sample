<!DOCTYPE html>
<html lang=ja>
  <head>
    <meta charset="UTF-8">
    <title>タイトルページ</title>
  </head>

  <body>
    <h1>タイトルページ</h1>

    <form method="GET" action="/show">
    <p>お名前は？：<br>
    <input type="text" name="username"></p>

    <p> 好きな麺類は何ですか？</p>
    <form>
    <select name="men">
      <option value="ramen">ラーメン</option>
      <option value="soba">そば</option>
      <option value="udon">うどん</option>
    </select>
    <input type="submit" value="送信する">
    </form>
  </body>

</html>