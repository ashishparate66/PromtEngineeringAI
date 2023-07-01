package practice;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.StringReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

import org.json.JSONArray;
import org.json.JSONObject;




public class ChatGPTExample {
    private static final String API_KEY = "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"; // Replace with your actual API key
    private static final String API_URL = "https://api.openai.com/v1/chat/completions";

    public static void main(String[] args) {
        System.out.println("Welcome to ChatGPT Application!");

        try (Scanner scanner = new Scanner(System.in)) {
            // Initialize conversation
            String conversationId = null;

            while (true) {
                System.out.print("User: ");
                String userMessage = scanner.nextLine();

                // Send user message and get AI response
                String aiResponse = getAIResponse(userMessage, conversationId);

                // Extract assistant reply from AI response
                String assistantReply = parseAssistantReply(aiResponse);

                // Print assistant reply
                System.out.println("Assistant: " + assistantReply);

                // Update conversation ID
                conversationId = parseConversationId(aiResponse);
            }
        }
    }

    private static String getAIResponse(String userMessage, String conversationId) {
        try {
            URL url = new URL(API_URL);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setRequestProperty("Authorization", "Bearer " + API_KEY);
            conn.setDoOutput(true);

            // Create request payload
            StringBuilder payload = new StringBuilder();
            if (conversationId != null) {
                payload.append("{\"messages\": [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"")
                        .append(userMessage).append("\"}], \"model\": \"gpt-3.5-turbo\", \"conversation_id\": \"")
                        .append(conversationId).append("\"}");
            } else {
                payload.append("{\"messages\": [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"")
                        .append(userMessage).append("\"}], \"model\": \"gpt-3.5-turbo\"}");
            }

            // Send request
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = payload.toString().getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            // Get response
            try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = br.readLine()) != null) {
                    response.append(line);
                }
                return response.toString();
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static String parseAssistantReply(String aiResponse) {
        // Parse the assistant's reply from the AI response
        // Customize this method based on the structure of the AI response
    	    JSONObject responseJson = new JSONObject(aiResponse);
    	    JSONArray choices = responseJson.getJSONArray("choices");
    	    JSONObject choice = choices.getJSONObject(0);
    	    String assistantReply = choice.getJSONObject("message").getString("content");
    	    return assistantReply;
    }

    private static String parseConversationId(String aiResponse) {
        // Parse the conversation ID from the AI response
        // Customize this method based on the structure of the AI response
        return null;
    }
}

