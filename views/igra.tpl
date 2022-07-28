% import model


<!DOCTYPE html>
<html>

<body>

  <h1>Besedle</h1>

  <h4> Preostali poskusi: {{igra.izpisi_rezultat()}} </h4>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  <form action='/igra/{{id_igre}}/' method='post'>
    Beseda: <input type='text' name='beseda'/>
    <button type='submit'>Ugibaj</button>
  </form>


</body>

</html>