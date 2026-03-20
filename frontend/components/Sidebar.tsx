"use client"

import {useState} from "react"

interface Topic{
  id:number
  title:string
  chapter:string
}

interface Props{
  topics:Topic[]
  onTopicClick:(id:number)=>void
}

export default function Sidebar({topics,onTopicClick}:Props){

  const [open,setOpen] = useState<{[key:string]:boolean}>({})

  const grouped = topics.reduce((acc:any,t:Topic)=>{

    if(!acc[t.chapter]){
      acc[t.chapter]=[]
    }

    acc[t.chapter].push(t)

    return acc

  },{})

  function toggle(chapter:string){

    setOpen(prev=>({
      ...prev,
      [chapter]:!prev[chapter]
    }))

  }

  return(

    <div className="w-72 border-r h-screen overflow-y-auto p-4">

      <h2 className="font-bold mb-4">
        Chapters
      </h2>

      {Object.keys(grouped).map(chapter=>(
        <div key={chapter} className="mb-3">

          <div
            className="font-semibold cursor-pointer"
            onClick={()=>toggle(chapter)}
          >
            {chapter}
          </div>

          {open[chapter] && grouped[chapter].map((t:Topic)=>(
            <div
              key={t.id}
              className="pl-4 py-1 text-sm cursor-pointer hover:bg-gray-100 rounded"
              onClick={()=>onTopicClick(t.id)}
            >
              {t.title}
            </div>
          ))}

        </div>
      ))}

    </div>

  )

}