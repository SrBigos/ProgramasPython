function funcioname(){
    var misdatitos = formulario.correato.value;
    var misdatitos2 = formulario.casilla.value;
    // var email = `email: ${misdatitos}`
    // var pedido = `id: ${misdatitos2}`
    // var dato = [];
    // dato.push(email);
    // dato.push(pedido);
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
