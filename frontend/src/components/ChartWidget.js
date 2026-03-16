
import {Bar} from 'react-chartjs-2'

export default function ChartWidget(){

const data={
 labels:['Math','Science','English'],
 datasets:[{label:'Marks',data:[80,75,90]}]
}

return <Bar data={data}/>
}
