 const btnEliminar = document.querySelectorAll('.btneliminar');

   (() => {
  'use strict'
  const forms = document.querySelectorAll('.needs-validation')
Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()       
      }

      form.classList.add('was-validated')
    }, false)
  })
  btnEliminar.forEach(btn=>{
    btn.addEventListener('click',function(e){
      let confrima= confirm("desea Eliminar curso")
      if (!confrima) {
         e.preventDefault();
      }
     
    })
  })

})()