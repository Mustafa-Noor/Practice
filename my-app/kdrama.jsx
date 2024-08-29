import React, {useState} from "react"
function KdramaList(){
    const [names, setNames] = useState(["My Demon", "Twinkling Watermelon"])

    function handleAddDrama(){
        const newName = document.getElementById('drama-name').value;
        document.getElementById('drama-name').value = "";
        if (newName !== ""){
            setNames(n => [...n, newName]);
        }
        
    }

    function HandleRemovalOfDrama(index){
        setNames(names.filter((elementt, i) => i !== index));
    }

    return(
        <div>
            <h2>Kdrama Names</h2>
            <ol>
                {names.map((name, index) => <li key={index} onClick={() => HandleRemovalOfDrama(index)}>{name}</li>)} 
                <input type="text" id="drama-name" placeholder="nameofdrama?"/>
                <button onClick={handleAddDrama}>Add</button>
            </ol>
        </div>
    )
}


export default KdramaList