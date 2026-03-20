"use client"

interface Chunk {

  text:string
  score:number
  title:string

}

export default function RagPanel({chunks}:{chunks:Chunk[]}){

  return(

    <div className="border-l w-96 p-4 overflow-scroll">

      <h2 className="font-bold mb-4">
        RAG Retrieval
      </h2>

      {chunks.map((c,i)=>(

        <div key={i} className="mb-6">

          <div className="text-sm text-gray-500">
            score: {c.score.toFixed(3)}
          </div>

          <div className="font-semibold">
            {c.title}
          </div>

          <div className="text-sm">
            {c.text.slice(0,200)}...
          </div>

        </div>

      ))}

    </div>

  )

}