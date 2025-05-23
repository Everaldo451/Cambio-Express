import axios from "axios"
import { CSRFType } from "@/types"

export let customAxios = axios.create()

export async function updateAxios (csrf_token:CSRFType|null) {
    customAxios = axios.create({
      headers: csrf_token?{
        'X-CSRFToken': csrf_token,
      }:{}
    })
}

