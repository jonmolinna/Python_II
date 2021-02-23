const btnDelete = document.querySelectorAll('.btn-delete');

if(btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', e => {
            if(!confirm('Are you sure you want to delete it?')){
                e.preventDefault();
            }
        })
    })
}


/*
    <link rel="stylesheet" href="{{ url for('static', filename='css/main.css')}}">

    <script src="{{url for('static' filename='js/main.js')}}"></script>
*/