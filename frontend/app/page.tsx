"use client"

import {useEffect,useState} from "react"

import Sidebar from "../components/Sidebar"
import ExplanationPanel from "../components/ExplanationPanel"
import RagPanel from "../components/RagPanel"

import { jsPDF } from "jspdf"

interface Topic{
  id:number
  title:string
  chapter:string
}

interface QA{
  q:string
  a:string
}

export default function Home(){

  const [topics,setTopics] = useState<Topic[]>([])
  const [lesson,setLesson] = useState("")
  const [sources,setSources] = useState<any[]>([])

  const [question,setQuestion] = useState("")
  const [qaHistory,setQaHistory] = useState<QA[]>([])

  // -------------------------
  // Load topics
  // -------------------------

  useEffect(()=>{

    async function loadTopics(){

      try{

        const res = await fetch("http://127.0.0.1:8000/topics")

        const data = await res.json()

        if(Array.isArray(data)){
          setTopics(data)
        }

      }catch(err){
        console.error("Topic load error:",err)
      }

    }

    loadTopics()

  },[])


  // -------------------------
  // Load lesson
  // -------------------------

  async function loadLesson(topicId:number){

    try{

      const res = await fetch("http://127.0.0.1:8000/lesson",{
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({
          topic_id:topicId,
          kid_mode:false
        })
      })

      const data = await res.json()

      setLesson(data.lesson)

      setSources(data.sources || [])

      setQaHistory([])

    }catch(err){
      console.error("Lesson error:",err)
    }

  }


  // -------------------------
  // Ask question
  // -------------------------

  async function ask(){

    if(!question.trim()) return

    try{

      const res = await fetch("http://127.0.0.1:8000/explain",{
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({question})
      })

      const data = await res.json()

      const newQA={
        q:question,
        a:data.answer
      }

      setQaHistory(prev=>[...prev,newQA])

      setSources(data.sources || [])

      setQuestion("")

    }catch(err){
      console.error("Question error:",err)
    }

  }


  // -------------------------
  // Export notes as PDF
  // -------------------------
function exportNotes(){

  const doc = new jsPDF()

  let y = 10
  const pageHeight = 280

  function checkPage(){

    if(y > pageHeight){
      doc.addPage()
      y = 10
    }

  }

  doc.text("Textbook Tutor Notes",10,y)
  y += 10

  doc.text("Lesson",10,y)
  y += 10

  const lessonLines = doc.splitTextToSize(lesson,180)

  lessonLines.forEach(line=>{
    checkPage()
    doc.text(line,10,y)
    y += 6
  })

  y += 6

  doc.text("Questions",10,y)
  y += 10

  qaHistory.forEach(item=>{

    const qLines = doc.splitTextToSize("Q: "+item.q,180)
    const aLines = doc.splitTextToSize("A: "+item.a,180)

    qLines.forEach(line=>{
      checkPage()
      doc.text(line,10,y)
      y += 6
    })

    aLines.forEach(line=>{
      checkPage()
      doc.text(line,10,y)
      y += 6
    })

    y += 4

  })

  doc.save("lesson_notes.pdf")

}
  

  return(

    <div className="flex h-screen">

      {/* Sidebar */}

      <Sidebar
        topics={topics}
        onTopicClick={loadLesson}
      />


      {/* Lesson column */}

      <div className="flex-1 flex flex-col">

        {/* Header */}

        <div className="p-6 border-b flex justify-between">

          <h1 className="text-3xl font-bold">
            Textbook Tutor
          </h1>

          <button
            className="bg-green-600 text-white px-4 py-2 rounded"
            onClick={exportNotes}
          >
            Export PDF
          </button>

        </div>


        {/* Lesson + Q&A */}

        <div className="flex-1 overflow-y-auto">

          <ExplanationPanel
            lesson={lesson}
            history={qaHistory}
          />

        </div>


        {/* Question box at bottom */}

        <div className="border-t p-4">

          <div className="flex gap-2">

            <input
              className="border p-2 flex-1"
              placeholder="Ask a question about this lesson"
              value={question}
              onChange={(e)=>setQuestion(e.target.value)}
            />

            <button
              className="bg-blue-500 text-white px-4 py-2 rounded"
              onClick={ask}
            >
              Ask
            </button>

          </div>

        </div>

      </div>


      {/* RAG Panel */}

      <RagPanel chunks={sources}/>

    </div>

  )

}