<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Graphviz Interactive</title>
</head>
<body>
  <h1> Interactive Graphviz </h1>
  <p> Try some of the examples from the
  <a href="http://graphviz.org/gallery/"> Graphviz Gallery </a>

  <hr>
  <form method="post" action="/dot">
    <textarea name="dot" rows="12" cols="60">{{dot}}</textarea>
    <input type="submit" value="Draw" name="target">
  </form>

{{! svg }}

% if err:
  <hr>
  <h2> Dot error: </h2>
  <p> {{err}} </p>
% end

</body>
</html>
