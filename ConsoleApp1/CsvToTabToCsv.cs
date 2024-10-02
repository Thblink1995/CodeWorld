namespace ConsoleApp1;

public static class CsvToTabToCsv
{
    public static string[][] CsvToTab(string filename)
    {
        List<string[]> rep = new List<string[]>();
        
        using (StreamReader file = new StreamReader(filename))
        {
            // Vérifie si le fichier est vide dès la lecture du header
            string? temp = file.ReadLine();
            if (temp == null) throw new ArgumentException($"{filename} is empty");

            // Lire les autres lignes jusqu'à la fin du fichier
            while ((temp = file.ReadLine()) != null)
            {
                string[] roughTab = temp.Split(',');
                rep.Add(roughTab);
            }
        }

        return rep.ToArray();
    }
    
    public static void TabToCsv(string filename, string[] tab)
    {
        using (StreamWriter file = new StreamWriter(filename))
        {
            // Écrire chaque élément du tableau sur une nouvelle ligne dans le fichier CSV
            foreach (string line in tab)
            {
                // Écrire la ligne dans le fichier
                file.WriteLine(line);
            }
        }
    }
}