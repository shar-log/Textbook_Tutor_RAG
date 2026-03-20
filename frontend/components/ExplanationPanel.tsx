"use client"

interface QA{
  q:string
  a:string
}

export default function ExplanationPanel({
  lesson,
  history
}:{lesson:string,history:QA[]}){

  return(

    <div className="p-6 overflow-y-auto">

      <h2 className="text-2xl font-bold mb-4">
        Lesson
      </h2>

      <div className="mb-8 whitespace-pre-wrap">
        {lesson || "Select a topic from the sidebar"}
      </div>

      <h3 className="text-xl font-semibold mb-3">
        Questions
      </h3>

      {history.map((item,i)=>(
        <div key={i} className="mb-6">

          <div className="font-semibold text-blue-600">
            Q: {item.q}
          </div>

          <div className="whitespace-pre-wrap">
            {item.a}
          </div>

        </div>
      ))}

    </div>

  )

}