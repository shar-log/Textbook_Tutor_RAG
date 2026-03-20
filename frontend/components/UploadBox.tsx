"use client"

import { useState } from "react"
import { uploadPDF } from "../lib/api"

export default function UploadBox() {

  const [file, setFile] = useState<File | null>(null)

  async function handleUpload() {

    if (!file) return

    console.log("[UPLOAD] Sending PDF")

    const res = await uploadPDF(file)

    console.log("[UPLOAD RESULT]", res)
  }

  return (
    <div className="border p-6 rounded-lg">

      <h2 className="text-xl font-bold mb-4">Upload Textbook</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e)=>setFile(e.target.files?.[0] || null)}
      />

      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded ml-3"
      >
        Upload
      </button>

    </div>
  )
}