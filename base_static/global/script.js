function show(){
    var dive = document.getElementById('overlay');
    dive.style.display = 'block';
}
function ocultModal() {
    var elemento = document.getElementById("overlay");
    elemento.style.display = 'none';
    console.log('Função foi chamada')
  }

function delete_contact() {
    console.log('Função chamada com sucesso')
    var form = document.getElementById('form_contact')
    form.submit()
    
}