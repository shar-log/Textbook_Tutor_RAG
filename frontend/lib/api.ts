export const API_BASE = "http://localhost:8000"

export async function uploadPDF(file: File) {

  const formData = new FormData()
  formData.append("file", file)

  const res = await fetch(`${API_BASE}/upload`, {
    method: "POST",
    body: formData
  })

  return res.json()
}

export async function explain(question: string) {

  const res = await fetch(`${API_BASE}/explain`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  })

  return res.json()
}