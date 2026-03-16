
import React,{useEffect,useState} from 'react'
import api from '../services/api'

export default function Students(){

const [students,setStudents] = useState([])

useEffect(()=>{
 api.get('/students/').then(res=>setStudents(res.data))
},[])

return(
<div>
<h2>Students</h2>
{students.map(s=>(
<div key={s.id}>{s.name}</div>
))}
</div>
)
}
