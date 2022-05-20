function funcioname(){
    var misdatitos = formulario.correato.value;
    var misdatitos2 = formulario.casilla.value;

    const dato = {
        email: misdatitos,
        id: misdatitos2
    }
    var data_string = JSON.stringify(dato);
    

    var file = new Blob([data_string], {type:"text"});
    var anchor = document.createElement('a');
    anchor.href = URL.createObjectURL(file);
    anchor.download = "datitos.json";
    anchor.click();
}
