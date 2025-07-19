<?php
namespace App\Service;

class OpenAiService
{
    private string $apiKey;
    private string $endpoint;

    public function __construct(string $apiKey, string $endpoint = 'https://api.openai.com/v1/chat/completions')
    {
        if (trim($apiKey) === '') {
            throw new \InvalidArgumentException("API key cannot be empty.");
        }
        $this->apiKey   = $apiKey;
        $this->endpoint = $endpoint;
    }

    public function ask(string $question): string
    {
        $q = trim($question);
        if ($q === '') {
            throw new \InvalidArgumentException("Please enter a question.");
        }

        $payload = [
            'model'       => 'gpt-3.5-turbo',
            'messages'    => [
                ['role'=>'system','content'=>"You are a professional fitness coach and certified nutritionist. Answer all health, fitness, and gym questions clearly and only in text. No emojis. No formatting."],
                ['role'=>'user',  'content'=> $q],
            ],
            'temperature' => 0.7,
        ];

        $json = $this->sendRequest($payload);
        $data = json_decode($json, true);

        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new \RuntimeException("Invalid JSON response: " . json_last_error_msg());
        }
        if (!isset($data['choices'][0]['message']['content'])) {
            throw new \RuntimeException("Unexpected API response structure.");
        }

        return $data['choices'][0]['message']['content'];
    }

    protected function sendRequest(array $payload): string
    {
        $ch = curl_init($this->endpoint);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER     => [
                'Content-Type: application/json',
                'Authorization: Bearer ' . $this->apiKey,
            ],
            CURLOPT_POST           => true,
            CURLOPT_POSTFIELDS     => json_encode($payload),
        ]);

        $resp   = curl_exec($ch);
        $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $err    = curl_error($ch);
        curl_close($ch);

        if ($resp === false) {
            throw new \RuntimeException("Error contacting OpenAI: $err");
        }
        if ($status < 200 || $status >= 300) {
            throw new \RuntimeException("OpenAI API returned HTTP status $status");
        }
        return $resp;
    }
}
